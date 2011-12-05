Name:           latrace
Version:        0.5.9
Release:        2%{?dist}
Summary:        LD_AUDIT feature frontend for glibc 2.4+
Group:          Development/Debuggers
License:        GPLv3+
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
URL:            http://people.redhat.com/jolsa/latrace
Source:         http://people.redhat.com/jolsa/latrace/dl/%{name}-%{version}.tar.bz2
ExclusiveArch:  %{ix86} x86_64 arm
BuildRequires:  autoconf bison asciidoc xmlto binutils-devel

%description
allows you to trace library calls and get their statistics in a
manner similar to the strace utility (syscall tracing)

%prep
%setup -q

%build
autoconf
%configure
make V=1

%install
rm -rf %{buildroot}
make install ROOTDIR=%{buildroot} V=1
chmod 0755 %{buildroot}/%{_libdir}/libltaudit.so.%{version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README ReleaseNotes TODO COPYING
%config(noreplace)  %{_sysconfdir}/*
%{_libdir}/libltaudit.so.%{version}
%{_bindir}/latrace
%{_bindir}/latrace-ctl
%{_mandir}/man1/*

%changelog
* Thu Jun 03 2010 Jiri Olsa <olsajiri@gmail.com> 0.5.9-2
- changing libltaudit.so permissions to 755

* Tue May 11 2010 Jiri Olsa <olsajiri@gmail.com> 0.5.9-1
- updated to new version

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.5.7-1.1
- Rebuilt for RHEL 6

* Tue Sep 08 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.7
- updated to new version
- upstream download moved

* Sun Jul 05 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.6-1
- updates based on the Fedora review comments

* Thu Jul 02 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.5-2
- minor updates based on the Fedora review comments

* Sat Jun 13 2009 Jiri Olsa <olsajiri@gmail.com> 0.5.5-1
- initial spec file
