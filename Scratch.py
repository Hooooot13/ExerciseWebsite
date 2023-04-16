'''
CREATE TYPE muscle AS ENUM ('abdominals','hamstrings','adductors','quadriceps','biceps','shoulders','chest','middle back','calves','glutes','lower back','lats','triceps','traps','forearms','neck','abductors');
CREATE TYPE forceType AS ENUM ('pull','push','static');
CREATE TYPE levelType AS ENUM ('beginner','intermediate','expert');
CREATE TYPE mechanicType AS ENUM ('compound','isolation');
CREATE TYPE equipmentType AS ENUM ('body only','machine','other','foam roll','kettlebells','dumbbell','cable','barbell','medicine ball','bands','exercise ball','e-z curl bar');
CREATE TYPE categoryType AS ENUM ('strength','stretching','plyometrics','strongman','powerlifting','cardio','olympic weightlifting');
'''

import psycopg2

conn = psycopg2.connect(database="exercises-db",
                            host="localhost",
                            user="postgres",
                            password="postgres",
                            port="5432")

muscleTypes = ['abdominals','hamstrings','adductors','quadriceps','biceps','shoulders','chest','middle back','calves','glutes','lower back','lats','triceps','traps','forearms','neck','abductors']
equipmentTypes = []
def selectMuscleANDSkillLevel_BodyWeightOnly(muscle, skillLevel, **hwargs):
    columns = ["name"]
    command = f"SELECT name "\
              f"FROM exercises " \
              f"WHERE \'{muscle}\' = ANY(primary_muscles) "\

    cursor.execute(command)
    for name in cursor.fetchall():
        print(name)

def CreateRandomWorkout_AllMuscles_BodyweightOnly(**kwargs):

    for muscle in musciles:
        command = f"SELECT name, primary_muscles, force "\
                  f"FROM exercises " \
                  f"WHERE \'{muscle}\' = ANY(primary_muscles) "\
                  #f"AND level IN (\'{skillLevel}\') " \
                  #f"AND equipment = \'body-only\';"
        for key, value in kwargs.items():
            command += f"AND {key} = \'{value}\' "

        command += ";"
        print(command)

class Wourkout:
    def __init__(self) -> None:
        self.Sets = {}
        self.musclesSelected = {}
        self.cursor = conn.cursor()
        self.muscleTypes = ['abdominals','hamstrings','adductors','quadriceps','biceps','shoulders','chest','middle back','calves','glutes','lower back','lats','triceps','traps','forearms','neck','abductors']

    def workoutBuilder(self):
        print(f"Select a musclegroup to exersise {self.muscleTypes}: ")
        exercise = self.selectExersiseByMuscle(input())

    def selectExersiseByMuscle(self, muscle):
        command = f"SELECT name, equipment, level, primary_muscles, secondary_muscles "\
                f"FROM exercises " \
                f"WHERE \'{muscle}\' = ANY(primary_muscles) "\

        self.cursor.execute(command)
        exercises = self.cursor.fetchall()
        for i, exercise in enumerate(exercises):
            print(f"{i} : {exercise}")
        return exercises[int(input("Seclect an exersice to add to your workout : "))]



if __name__ == '__main__':
    _workout = Wourkout()
    _workout.workoutBuilder()