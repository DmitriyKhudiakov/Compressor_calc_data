from classes.SectionData import SectionData


class EnterMassFlowData:
    def __init__(self, data_name):
        self.name = data_name
        # section list
        self.sec = []

    def add_section(self, dl):
        self.sec.append(SectionData(dl[0], dl[1], dl[2], dl[3], dl[4], dl[5], dl[6], dl[7], dl[8]))
