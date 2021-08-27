fig, axes = plt.subplots(figsize=(20, 20), dpi=120, nrows=7, ncols=2)

ax0 = X.iloc[::1500,0:4].plot(ax=axes[0,0])
ax0.set_xlim([0,220320])
ax0.grid()
ax0.set_xlabel('Time [minutes]')

ax1 = X.iloc[::1500,4:8].plot(ax=axes[0,1])
ax1.set_xlim([0,220320])
ax1.grid()
ax1.set_xlabel('Time [minutes]')

ax2 = X.iloc[::1500,8:12].plot(ax=axes[1,0])
ax2.set_xlim([0,220320])
ax2.grid()
ax2.set_xlabel('Time [minutes]')

ax3 = X.iloc[::1500,12:16].plot(ax=axes[1,1])
ax3.set_xlim([0,220320])
ax3.grid()
ax3.set_xlabel('Time [minutes]')

ax4 = X.iloc[::1500,16:20].plot(ax=axes[2,0])
ax4.set_xlim([0,220320])
ax4.grid()
ax4.set_xlabel('Time [minutes]')

ax5 = X.iloc[::1500,20:24].plot(ax=axes[2,1])
ax5.set_xlim([0,220320])
ax5.grid()
ax5.set_xlabel('Time [minutes]')

ax6 = X.iloc[::1500,24:28].plot(ax=axes[3,0])
ax6.set_xlim([0,220320])
ax6.grid()
ax6.set_xlabel('Time [minutes]')

ax7 = X.iloc[::1500,28:32].plot(ax=axes[3,1])
ax7.set_xlim([0,220320])
ax7.grid()
ax7.set_xlabel('Time [minutes]')

ax8 = X.iloc[::1500,32:36].plot(ax=axes[4,0])
ax8.set_xlim([0,220320])
ax8.grid()
ax8.set_xlabel('Time [minutes]')

ax9 = X.iloc[::1500,36:40].plot(ax=axes[4,1])
ax9.set_xlim([0,220320])
ax9.grid()
ax9.set_xlabel('Time [minutes]')

ax10 = X.iloc[::1500,40:44].plot(ax=axes[5,0])
ax10.set_xlim([0,220320])
ax10.grid()
ax10.set_xlabel('Time [minutes]')

ax11 = X.iloc[::1500,44:48].plot(ax=axes[5,1])
ax11.set_xlim([0,220320])
ax11.grid()
ax11.set_xlabel('Time [minutes]')

ax12 = X.iloc[::1500,48:52].plot(ax=axes[6,0])
ax12.set_xlim([0,220320])
ax12.grid()
ax12.set_xlabel('Time [minutes]')

plt.tight_layout()
