class MovieTitle:

    def __init__(self, primaryTitle, originalTitle, runtimeMinutes):
        self.primary_title = primaryTitle
        self.original_title = originalTitle
        self.runtime_minutes = runtimeMinutes

    @staticmethod
    def create_from_dict(lookup):
        return MovieTitle(
            lookup["primaryTitle"],
            lookup["originalTitle"],
            lookup["runtimeMinutes"]
        )
