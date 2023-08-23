import time
import os

starttimmer = time.time()


for x in range(100000):
    f = open("filename.txt", "a")
    f.write("Random text \n")

os.remove("filename.txt")
endtimmer = time.time()
print(f"Time taken by this program is : {endtimmer-starttimmer}")
