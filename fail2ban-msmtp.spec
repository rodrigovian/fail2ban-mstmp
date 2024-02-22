Name: fail2ban-msmtp
Version: 0.0.1
Release: 1%{?dist}
Summary: Msmtp actions for Fail2Ban
URL: https://github.com/rodrigovian/fail2ban-mstmp
License: GPLv2+
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz

Requires(pre): fail2ban
Requires: msmtp 
Requires: whois

################################################################################
%description
This package installs Fail2Ban's msmtp actions.  

################################################################################
%prep
%setup -q

################################################################################
%build
echo "Build OK"

################################################################################
%install
[ "%{buildroot}" != '/' ] && %{__rm} -rf %{buildroot}

# Create struct
%{__mkdir_p} %{buildroot}%{_sysconfdir}/fail2ban/action.d

# Copy files
%{__install} -m 0644 src/msmtp.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-buffered.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-common.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-geoip-lines.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-whois.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-whois-ipjailmatches.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-whois-ipmatches.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-whois-lines.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/
%{__install} -m 0644 src/msmtp-whois-matches.conf %{buildroot}%{_sysconfdir}/fail2ban/action.d/

################################################################################
%clean
[ "%{buildroot}" != '/' ] && %{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)

%{_sysconfdir}/fail2ban/action.d/msmtp.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-buffered.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-common.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-geoip-lines.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-whois.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-whois-ipjailmatches.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-whois-ipmatches.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-whois-lines.conf
%{_sysconfdir}/fail2ban/action.d/msmtp-whois-matches.conf

################################################################################
%changelog
* Thu Feb 22 2024 Rodrigo Vian <rodrigovian@gmail.com> - 0.0.1
- Initial version.
