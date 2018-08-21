# Alerting

We can set up a notification system to let users/admins know that a pattern match has occurred.

* Logstash output plugin alerting via (Email, Pager duty, JIRA, etc.)
* An open source alerting for elasticsearch by Yelp called elastalert
* Another open source project by Etsy 411
* X-Pack (commerical offering by Elastic)
* Custom scripts

### ElastAlert

> ElastAlert is a simple framework for alerting on anomalies, spikes, or other patterns of interest from data in Elasticsearch.

* Simple ElastAlert rule to detect new certstream logs certificates

```yaml
es_host: localhost
es_port: 9200
name: "New certificate alert"
type: frequency
index: filebeat-*
num_events: 10
timeframe:
  minutes: 1

# For more info: http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl.html

filter:
- query:
    query_string:
      query: 'tags: "certstream" AND name: "*.ietf.org"'

alert:
  - slack

slack:
slack_webhook_url: "https://hooks.slack.com/services/xxxxx"
slack_username_override: "alert-bot"
slack_emoji_override: "robot_face"

realert:
  minutes: 0
```

**Rule Types**

* Any
* Blacklist
* Whitelist
* Change
* Frequency
* Spike
* Flatline
* New Term
* Cardinality
* Metric Aggregation
* Percentage Match

**Alert Types**

* Command, HTTP POST
* Email, SNS, Stomp
* Jira, Gitter, ServiceNow
* OpsGenie, VictorOps, PagerDuty
* Twilio, Telegram
* HipChat, Slack, MS Teams