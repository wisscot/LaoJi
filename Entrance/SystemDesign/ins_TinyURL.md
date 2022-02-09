
# Design Tiny URL

# Scenario

100M DAU
Everyuser generate 0.1 message contains url
Average write QPS = 100M * 0.1 /3600/24 = ~100
Peak QPS ~300

Everyuser click 1 tiny url everyday
Aerage read QPS = 100M * 1 / 3600/24 = ~ 1k
Peak QPS ~3k

Space Requirement
100M * 0.1 ~ 10M urls
average length 100 Bytes -> 1 GB / day 

# Service

UrlService
  - UrlService.encode(long_url)
  - UrlService.decode(short_url)

# Storage 

do not need much