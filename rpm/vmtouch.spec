Name:       vmtouch
Summary:    Tool to touch and lock files into memory    
Release:    1
Group:      System/Daemons
License:    BSD
URL:        http://hoytech.com/vmtouch/
Version:    0.0
Source0:    %{name}-%{version}.tar.bz2

%description
vmtouch is a tool that can touch and lock files into memory

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
gcc -Wall -O3 -o vmtouch vmtouch.c

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin/
cp vmtouch %{buildroot}/usr/bin/

%files
%defattr(-,root,root,-)
%{_bindir}/vmtouch

