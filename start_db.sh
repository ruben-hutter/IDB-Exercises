#!/bin/bash

CONTAINER_NAME="introdb-postgres"

# Check if the container is already running
if [ "$(sudo docker inspect -f '{{.State.Running}}' $CONTAINER_NAME 2>/dev/null)" == "true" ]; then
	echo "Container $CONTAINER_NAME is already running."
else
	# Start the container
	sudo docker start $CONTAINER_NAME
	echo "Container $CONTAINER_NAME started."
fi
