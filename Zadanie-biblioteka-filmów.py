class Movies:
    def __init__(self,Title,Relased_year,Genre,Numer_of_views):
        self.Title = Title
        self.Relased_year = Relased_year
        self.Genre = Genre
        self.Numer_of_views = Numer_of_views

        self.Current_number_of_views = 0

    def play(self, view=1):
        self.Current_number_of_views +=view
    def __str__(self):
        return f"Title:{self.Title}, Relased_year:{self.Relased_year}"

class Series(Movies):
    def __init__(self,Title,Relased_year,Genre,Numer_of_views,Series_id,Episode_id):
        super().__init__(Title,Relased_year,Genre,Numer_of_views)
        self.Series_id = Series_id
        self.Episode_id = Episode_id

    def play(self, view=1):
        return super().play(view)
    def __str__(self):
        return f"{self.Title} {self.Series_id}{self.Episode_id}"