Y = one_hot['NORMAL']
data = pd.concat([X_fitted.iloc[:, 0:8],Y], axis=1, sort=False)

# Data visualisation imposing machine status information
fig, axes = plt.subplots(figsize=(20, 5), dpi=120, nrows=1, ncols=2)

ax0 = data.iloc[::1500, 0:4].plot(ax=axes[0])
ax0 = data.iloc[::1500, -1].plot(drawstyle="steps", ax=axes[0])
ax0.set_xlim([0,220320])
ax0.grid()
ax0.set_xlabel('Time [minutes]')

ax1 = data.iloc[::1500,4:8].plot(ax=axes[1])
ax1 = data.iloc[::1500, -1].plot(drawstyle="steps",ax=axes[1])
ax1.set_xlim([0,220320])
ax1.grid()
ax1.set_xlabel('Time [minutes]')

plt.tight_layout
