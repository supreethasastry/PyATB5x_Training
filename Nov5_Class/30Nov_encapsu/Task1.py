class PersonalDiary:
        def __init__(self):
            self.name="Supreetha"
            self.__contents_Page="Affirmations, Journaling and Drifting thoughts"

        def display_diaryowner(self):
            print(self.name)

        def display_diarycontents_Page(self):
            print("Contents Page: ")
            print(self.__contents_Page)

s=PersonalDiary()
s.display_diaryowner()
s.display_diarycontents_Page()