import math as m


class ResMassFlowData:
    def __init__(self, enter_data, u, d2, r, c_p):
        self.u = u
        self.d2 = d2
        self.cu = None
        self.R = r
        self.c_p = c_p
        self.ed = enter_data
        # result parameters
        self.Phi = None
        self.psi_T = None
        self.n_impeller = None
        self.hp_impeller = None
        self.hd_impeller = None
        self.hi_impeller = None
        self.eta_p_impeller = None
        self.eta_p_f_impeller = None
        self.ratio_P_impeller = None
        self.ratio_P_f_impeller = None
        self.psi_i_impeller = None
        self.n_stage = None
        self.hp_stage = None
        self.hd_stage = None
        self.hi_stage = None
        self.eta_p_stage = None
        self.eta_p_f_stage = None
        self.ratio_P_stage = None
        self.ratio_P_f_stage = None
        self.psi_i_stage = None

    def calc_phi(self):
        self.Phi = self.ed.sec[0].m / (self.ed.sec[0].rho * m.pi * self.u * self.d2 ** 2 / 4.0)

    def calc_psi_t(self):
        self.cu = m.sqrt(self.ed.sec[2].c ** 2 - self.ed.sec[2].cr ** 2)
        self.psi_T = self.cu / self.u

    def calc_n_impeller(self):
        help1 = self.ed.sec[2].p / self.ed.sec[0].p
        help2 = self.ed.sec[2].t / self.ed.sec[0].t
        self.n_impeller = (m.log(help1, 10.0)) / (m.log(help2, 10.0))

    def calc_hp_impeller(self):
        self.hp_impeller = self.n_impeller * self.R * self.ed.sec[0].t * (
                (self.ed.sec[2].p / self.ed.sec[0].p) ** (1.0 / self.n_impeller) - 1.0)

    def calc_hd_impeller(self):
        self.hd_impeller = (self.ed.sec[2].c ** 2 - self.ed.sec[0].c ** 2) / 2.0

    def calc_hi_impeller(self):
        self.hi_impeller = self.c_p * (self.ed.sec[2].t_f - self.ed.sec[0].t_f)

    def calc_eta_p_impeller(self):
        self.eta_p_impeller = self.hp_impeller / (self.hi_impeller - self.hd_impeller)

    def calc_eta_p_f_impeller(self):
        self.eta_p_f_impeller = (self.hp_impeller + self.hd_impeller) / self.hi_impeller

    def calc_ratio_p_impeller(self):
        self.ratio_P_impeller = self.ed.sec[2].p / self.ed.sec[0].p

    def calc_ratio_p_f_impeller(self):
        self.ratio_P_f_impeller = self.ed.sec[2].p_f / self.ed.sec[0].p_f

    def calc_psi_i_impeller(self):
        self.psi_i_impeller = self.hi_impeller / (self.u ** 2.0)

    def calc_n_stage(self):
        help1 = self.ed.sec[7].p / self.ed.sec[0].p
        help2 = self.ed.sec[7].t / self.ed.sec[0].t
        self.n_stage = (m.log(help1, 10.0)) / (m.log(help2, 10.0))

    def calc_hp_stage(self):
        self.hp_stage = self.n_stage * self.R * self.ed.sec[0].t * (
                (self.ed.sec[7].p / self.ed.sec[0].p) ** (1.0 / self.n_stage) - 1.0)

    def calc_hd_stage(self):
        self.hd_stage = (self.ed.sec[7].c ** 2 - self.ed.sec[0].c ** 2) / 2.0

    def calc_hi_stage(self):
        self.hi_stage = self.c_p * (self.ed.sec[7].t_f - self.ed.sec[0].t_f)

    def calc_eta_p_stage(self):
        self.eta_p_stage = self.hp_stage / (self.hi_stage - self.hd_stage)

    def calc_eta_p_f_stage(self):
        self.eta_p_f_stage = (self.hp_stage + self.hd_stage) / self.hi_stage

    def calc_ratio_p_stage(self):
        self.ratio_P_stage = self.ed.sec[7].p / self.ed.sec[0].p

    def calc_ratio_p_f_stage(self):
        self.ratio_P_f_stage = self.ed.sec[7].p_f / self.ed.sec[0].p_f

    def calc_psi_i_stage(self):
        self.psi_i_stage = self.hi_stage / (self.u ** 2.0)

    def calc_parameters(self):
        try:
            self.calc_phi()
            self.calc_psi_t()
            self.calc_n_impeller()
            self.calc_hp_impeller()
            self.calc_hd_impeller()
            self.calc_hi_impeller()
            self.calc_eta_p_impeller()
            self.calc_eta_p_f_impeller()
            self.calc_ratio_p_impeller()
            self.calc_ratio_p_f_impeller()
            self.calc_psi_i_impeller()
            self.calc_n_stage()
            self.calc_hp_stage()
            self.calc_hd_stage()
            self.calc_hi_stage()
            self.calc_eta_p_stage()
            self.calc_eta_p_f_stage()
            self.calc_ratio_p_stage()
            self.calc_ratio_p_f_stage()
            self.calc_psi_i_stage()
        except:
            return False
        return True
