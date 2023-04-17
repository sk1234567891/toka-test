# Use a base image with Ansible installed
FROM python:3.9-slim-buster

# Copy the Ansible playbook and variable files to the container
COPY ./playbook.yaml .
COPY ./config.yaml .
COPY ./entrypoint.bash .

# Install dependencies for the Ansible playbook
RUN pip install --no-cache-dir ansible

# Set the default command to run the Ansible playbook
CMD [ "./entrypoint.bash" ]

