FROM python:latest



WORKDIR /workspace

# Copy the entire project and build it

COPY . /workspace
RUN pip install -r requirements.txt

#ENTRYPOINT ["/bin/project"]
# Args to project
#CMD ["--help"]

