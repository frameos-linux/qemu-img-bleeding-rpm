Name: qemu-img-bleeding
Version: git20111027
Release: 1%{?dist}
Group: Applications/System
Summary: QEMU disk image utility
License: GPL 
URL: http://qemu.org
Source: qemu-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: zlib-devel
BuildRequires: glib2-devel

%description
Bleeding edge version of the qemu-img command from QEMU.

%prep
%setup -q -n qemu-%{version}

%build
./configure
%{__make} qemu-img 

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 0755 qemu-img %{buildroot}/%{_bindir}/qemu-img-bleeding

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc LICENSE 
%{_bindir}

%changelog
* Thu Oct 27 2011 Sergio Rubio <rubiojr@frameos.org> - 20111027-1
- qemu-img-bleeding.spec
