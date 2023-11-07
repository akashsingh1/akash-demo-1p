import os
import shutil

M2_REPO_PATH = os.path.expanduser("~/.m2/repository")

dependencylist = []

def parse_and_print_remote_repositories(repo_path):
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith('_remote.repositories'):
                file_path = os.path.join(root, file)
                #print(f"Contents of {file_path}:\n")
                with open(file_path, 'r') as f:
                    content = f.read()
                    if("central" not in content):
                        #print(f"Contents of {file_path}:\n")
                        #print(content)
                        f.seek(0)
                        for line in f:
                            if line.strip().startswith('#'):
                                continue
                            if '.jar' or '.pom' or '.war' in line:
                                print(line, end='')
                                dependencylist.append(file_path)
    print(dependencylist)

def move_file_with_structure(source_path, target_directory):
    abs_source_path = os.path.abspath(source_path)
    
    root_path, path_to_file = os.path.splitdrive(abs_source_path)
    
    full_local_path = os.path.join(target_directory, path_to_file.lstrip(os.sep))
    
    os.makedirs(os.path.dirname(full_local_path), exist_ok=True)
    
    shutil.copy2(abs_source_path, full_local_path)
    
    print(f"Moved {abs_source_path} to {full_local_path}")


if __name__ == "__main__":
    parse_and_print_remote_repositories(M2_REPO_PATH)

# destination = "/Users/akash/Documents"
# for path in dependencylist:
#     print(path)
#     move_file_with_structure(path, destination)



import subprocess

output_file = 'dependency-tree.txt'

cmd = ['mvn', 'dependency:tree']

with open(output_file, 'w') as f:
    subprocess.run(cmd, stdout=f, text=True)

print(f"Output saved to {output_file}")



