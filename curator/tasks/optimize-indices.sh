#!/bin/bash

curator --host $ELASTICSEARCH_HOST --port $ELASTICSEARCH_PORT optimize --max_num_segments 1 indices --prefix logstash --older-than 1 --time-unit days --timestring '%Y.%m.%d'
