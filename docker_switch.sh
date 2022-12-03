RUNNING_1="$(docker inspect -f '{{.State.Status}}' s8c_sauth_1)"
RUNNING_2="$(docker inspect -f '{{.State.Status}}' s8c_sauth-redis_1)"
RUNNING_3="$(docker inspect -f '{{.State.Status}}' s8c_traefik_1)"
RUNNING_4="$(docker inspect -f '{{.State.Status}}' s8c_chat-redis_1)"
RUNNING_5="$(docker inspect -f '{{.State.Status}}' s8c_couchbase_1)"

if [ "$RUNNING_1" = "running" ] && [ "$RUNNING_2" = "running" ] && [ "$RUNNING_3" = "running" ] && [ "$RUNNING_4" = "running" ] && [ "$RUNNING_5" = "running" ]; then 
docker stop s8c_couchbase_1
docker stop s8c_chat-redis_1
docker stop s8c_traefik_1
docker stop s8c_sauth-redis_1
docker stop s8c_sauth_1
else
docker start s8c_couchbase_1
docker start s8c_chat-redis_1
docker start s8c_traefik_1
docker start s8c_sauth-redis_1
docker start s8c_sauth_1
fi