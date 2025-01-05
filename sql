WITH
    timeRange AS (
        SELECT 
            (toUInt64(1735879788010000000) - toUInt64(1735858188010000000)) / 1000000000.0 AS seconds
    ),
    processed_traces AS (
        SELECT
            resource_string_service$$name AS service_name,
            name AS span_name,
            CASE
                WHEN attribute_string_messaging$$system = 'kafka' THEN 'kafka'
                WHEN (has(attributes_string, 'celery.action') OR has(attributes_string, 'celery.task_name')) THEN 'celery'
                ELSE 'other'
            END AS messaging_system,
            COALESCE(
                NULLIF(attributes_string['messaging.destination.name'], ''),
                NULLIF(attributes_string['messaging.destination'], '')
            ) AS destination,
            kind_string,
            durationNano,
            status_code
        FROM
            signoz_traces.distributed_signoz_index_v3
        WHERE
            timestamp >= toDateTime64(1735858188010000000 / 1000000000.0, 9)
            AND timestamp <= toDateTime64(1735879788010000000 / 1000000000.0, 9)
            AND (
                attribute_string_messaging$$system = 'kafka'
                OR
                has(attributes_string, 'celery.action')
                OR
                has(attributes_string, 'celery.task_name')
            )
    ),
    aggregated_metrics AS (
        SELECT
            service_name,
            span_name,
            messaging_system,
            destination,
            kind_string,
            count(*) AS total_count,
            sumIf(1, status_code = 2) AS error_count,
            quantile(0.95)(durationNano) / 1000000 AS p95_latency
        FROM
            processed_traces
        GROUP BY
            service_name,
            span_name,
            messaging_system,
            destination,
            kind_string
    )
SELECT
    service_name,
    span_name,
    messaging_system,
    destination,
    kind_string AS kind,
    COALESCE(total_count / timeRange.seconds, 0) AS rate,
    COALESCE((error_count * 100.0) / total_count, 0) AS error_percentage,
    p95_latency
FROM
    aggregated_metrics,
    timeRange
WHERE
    messaging_system IN ('kafka', 'celery')
ORDER BY
    service_name,
    span_name;
