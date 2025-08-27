# from loguru import logger

result=[]

test_tuple = ([5,7],[6,7,8,9],[3])

for sublist in test_tuple:
     for element in sublist:
          result.append(element)

# logger.info(f"the falt tuple in the :{tuple(result)}")
print(tuple(result))