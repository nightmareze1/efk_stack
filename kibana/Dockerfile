# https://github.com/elastic/kibana-docker
FROM docker.elastic.co/kibana/kibana-oss:6.3.0

# Search Guard plugin
# https://docs.search-guard.com/latest/search-guard-versions
# https://search.maven.org/search?q=g:com.floragunn%20AND%20a:search-guard-kibana-plugin&core=gav
ENV SG_VERSION=6.3.0-14
RUN kibana-plugin install https://repo1.maven.org/maven2/com/floragunn/search-guard-kibana-plugin/6.3.0-14/search-guard-kibana-plugin-6.3.0-14.zip

# Add your kibana plugins setup here
# Example: RUN kibana-plugin install <name|url>
