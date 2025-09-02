docker build -t yutou/fastlivo2 .

docker image prune -f  # 强制清理none镜像

# docker build -t yutou/fastlivo2 . --no-cache  #  无缓存构建镜像