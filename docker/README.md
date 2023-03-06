#Build ansible image and run the container.
docker build -f ansible_in_container -t ansible:latest .
docker run -dt --name ansible-in-container ansible:latest

#Build terraform image and run the container.
docker build -f terraform_in_container -t terraform:latest .
docker run -dt --name ansible-container terraform:latest

