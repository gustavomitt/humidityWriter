#!/usr/bin/env python

from gcloud import pubsub

client = pubsub.Client()

topics, token = client.list_topics() 
for t in topics:
  if t.full_name == "projects/gardencontrolarduino/topics/humidity":
    topic=t

subs = topic.subscription("sub")
subs.create()

pulled = subs.pull(max_messages=100)
for ack, message in pulled:
  print message.data


