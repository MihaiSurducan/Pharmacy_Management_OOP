class MedicamentValidationError(Exception):
    pass


class MedicamentValidator:

    def validate(self, Medicament):
        errors = []
        if Medicament.recipe not in [True, False]:
            errors.append('Require recipe must be one of the following: Yes or No')

        if errors != []:
            raise MedicamentValidationError(errors)
