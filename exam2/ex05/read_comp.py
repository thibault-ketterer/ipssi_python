
for line in open("docker-compose.yml"):
    if "image" in line:
        print(line.split(':')[1].strip())
