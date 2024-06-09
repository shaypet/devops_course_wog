from utils import get_score,SCORES_FILE_NAME
def add_score(score):
   file_path = f'{SCORES_FILE_NAME}'
   current_score = get_score()

   file = open(file_path, "w")
   new_score=score + (current_score or 0) # if none decimal value is return, or file error (None) add zero to score, else, the current score in file
   file.write(str(new_score))
   file.close()
