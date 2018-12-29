# efk_stack
EFK Stack with Docker-Compose
```
[root@ip-10-91-41-215 elk]# docker-compose up --build -d
Creating network "elk_default" with the default driver
Building elasticsearch
Step 1/2 : FROM elasticsearch:5.5.2
 ---> d1ac13423d3c
Step 2/2 : RUN elasticsearch-plugin install --batch repository-s3
 ---> Using cache
 ---> c460367269f5
Successfully built c460367269f5
Successfully tagged elk_elasticsearch:latest
Building fluentd
Step 1/2 : FROM fluent/fluentd:v0.12-debian
 ---> 3bcd4366c0e6
Step 2/2 : RUN ["gem", "install", "fluent-plugin-elasticsearch", "--no-rdoc", "--no-ri", "--version", "1.9.2"]
 ---> Using cache
 ---> 272e7d301430
Successfully built 272e7d301430
Successfully tagged elk_fluentd:latest
Building curator
Step 1/10 : FROM gliderlabs/alpine:3.2
 ---> dfd25d204c70
Step 2/10 : ENV CURATOR_VERSION 3.4.0
 ---> Using cache
 ---> 776899479af1
Step 3/10 : RUN apk --update add python py-pip bash && pip install --upgrade  elasticsearch-curator==$CURATOR_VERSION
 ---> Using cache
 ---> 24a161fa2450
Step 4/10 : ADD docker-entrypoint.sh /
 ---> Using cache
 ---> 4f9791f57664
Step 5/10 : ADD tasks/optimize-indices.sh /etc/periodic/
 ---> Using cache
 ---> 31989ba9380f
Step 6/10 : ADD tasks/purge-old-indices.sh /etc/periodic/
 ---> Using cache
 ---> d700ca4aae55
Step 7/10 : RUN printf "\n*/5\t*\t*\t*\t*\t/etc/periodic/purge-old-indices.sh" >> /etc/crontabs/root
 ---> Using cache
 ---> 61a3b5d0d67d
Step 8/10 : RUN printf "\n*/5\t*\t*\t*\t*\t/etc/periodic/optimize-indices.sh" >> /etc/crontabs/root
 ---> Using cache
 ---> b48f52d15e1c
Step 9/10 : ENTRYPOINT ["/docker-entrypoint.sh"]
 ---> Using cache
 ---> 02a38abcb8db
Step 10/10 : CMD ["crond", "-f", "-l", "8"]
 ---> Using cache
 ---> b5a7852c8774
Successfully built b5a7852c8774
Successfully tagged elk_curator:latest
Creating elk_elasticsearch_1_48cd26c0f2b7 ... done
Creating elk_fluentd_1_1b266c2d6f1c       ... done
Creating elk_kibana_1_3eff7de6eded        ... done
Creating elk_curator_1_665081df3947       ... done

[root@ip-10-91-41-215 elk]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                                                                  NAMES
06a05295c5f2        elk_fluentd         "tini -- /bin/entryp…"   5 seconds ago       Up 2 seconds        0.0.0.0:9880->9880/tcp, 5140/tcp, 0.0.0.0:24224->24224/tcp, 0.0.0.0:24224->24224/udp   elk_fluentd_1_415173ea4f7c
6855691b6107        elk_curator         "/docker-entrypoint.…"   5 seconds ago       Up 2 seconds                                                                                               elk_curator_1_be9c765c0947
bb2df4424c67        kibana:5.5          "/docker-entrypoint.…"   5 seconds ago       Up 3 seconds        0.0.0.0:5601->5601/tcp                                                                 elk_kibana_1_4d0385478295
553faf7ff35f        elk_elasticsearch   "/docker-entrypoint.…"   6 seconds ago       Up 5 seconds        0.0.0.0:9200->9200/tcp, 0.0.0.0:9300->9300/tcp                                         elk_elasticsearch_1_5b663ec85bc2
```
Check EFK_STACK Running:
![alt text](https://raw.githubusercontent.com/nightmareze1/efk_stack/master/img/3.png)

![alt text](https://raw.githubusercontent.com/nightmareze1/efk_stack/master/img/2.png)
