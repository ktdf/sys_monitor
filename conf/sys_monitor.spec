Name:           sys_monitor
Version:        1.0
Release:        0.1
Summary:        Sys_monitor test task

License:        NONE
URL:            https://example.com/%{name}
Source0:        https://example.com/%{name}/release/%{name}-%{version}.tar.gz

Requires:       python3-psutil
Requires:	logrotate

BuildArch:	noarch

%description
sys_monitor logging package written on python as a test task


%prep
%setup -q


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
install -m 0644 %{name}.conf %{buildroot}/%{_sysconfdir}/%{name}.conf
install -m 0644 %{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
install -m 0644 %{name}.service %{buildroot}/%{_sysconfdir}/systemd/system

%files
%{_bindir}/%{name}
%{_sysconfdir}/%{name}.conf
%{_sysconfdir}/logrotate.d/%{name}
%{_sysconfdir}/systemd/system/%{name}.service
