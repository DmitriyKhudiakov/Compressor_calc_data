import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import sort_data_list_by_mass_flow as sort_data


def plt_1(res_data_list):
    plt.title("$\eta_{п} ,\eta_{п}^{*} = f\left(\Phi\\right)$")
    plt.grid()
    plt.ylim([0.0, 1.0])
    plt.plot([i.Phi for i in res_data_list], [i.eta_p_impeller for i in res_data_list], label="$\eta_{п.рк}$")
    plt.plot([i.Phi for i in res_data_list], [i.eta_p_stage for i in res_data_list], label="$\eta_{п.ст}$")
    plt.plot([i.Phi for i in res_data_list], [i.eta_p_f_impeller for i in res_data_list], label="$\eta_{п.ст}^{*}$")
    plt.plot([i.Phi for i in res_data_list], [i.eta_p_f_stage for i in res_data_list], label="$\eta_{п.ст}^{*}$")
    plt.legend()


def plt_2(res_data_list):
    plt.title("$\Pi ,\Pi^{*} = f\left(\Phi\\right)$")
    plt.grid()
    plt.plot([i.Phi for i in res_data_list], [i.ratio_P_impeller for i in res_data_list], label="$\Pi_{рк}$")
    plt.plot([i.Phi for i in res_data_list], [i.ratio_P_stage for i in res_data_list], label="$\Pi_{ст}$")
    plt.plot([i.Phi for i in res_data_list], [i.ratio_P_f_impeller for i in res_data_list], label="$\Pi_{рк}^{*}$")
    plt.plot([i.Phi for i in res_data_list], [i.ratio_P_f_stage for i in res_data_list], label="$\Pi_{ст}^{*}$")
    plt.legend()


def plt_3(res_data_list):
    plt.title("$\psi_{i},\psi_{т} = f\left(\Phi\\right)$")
    plt.grid()
    plt.ylim([0.0, 1.0])
    plt.plot([i.Phi for i in res_data_list], [i.psi_i_impeller for i in res_data_list], label="$\psi_{i.рк}$")
    plt.plot([i.Phi for i in res_data_list], [i.psi_i_stage for i in res_data_list], label="$\psi_{i.ст}$")
    plt.plot([i.Phi for i in res_data_list], [i.psi_T for i in res_data_list], label="$\psi_{т}$")
    plt.legend()


def plot(res_data_list):
    res_data_list = sort_data.sort_res_data_by_mass_flow(res_data_list)
    gs = gridspec.GridSpec(2, 2)
    plt.figure()
    ax = plt.subplot(gs[0, 0])
    plt_1(res_data_list)
    ax = plt.subplot(gs[0, 1])
    plt_2(res_data_list)
    ax = plt.subplot(gs[1, :])
    plt_3(res_data_list)
    plt.show()
