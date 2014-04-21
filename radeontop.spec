%global commit eadc100956fb5e346a4c5726453efd15fb2ec9f7
%global commitdate 20140421
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitversion .git%{commitdate}.%{shortcommit}

Summary:    View GPU utilization off AMD/ATI Radeon devices
Name:       radeontop
Version:    0.7
Release:    1%{?gitversion}%{?dist}
License:    GPLv3
Group:      System Environment/Libraries
URL:        https://github.com/clbr/%{name}

Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: asciidoc gettext
BuildRequires: ncurses-devel
BuildRequires: libpciaccess-devel

%description
RadeonTop shows the utilization of your GPU, both in general and by blocks.

Supported cards are R600 and up.


%prep
%setup -q -n %{name}-%{commit}


%build
# configure doesn't exist, but we need the exported CFLAGS and friends
%configure || :
make %{?_smp_mflags} PREFIX=%{_prefix}


%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%doc README.md TODO COPYING
%{_sbindir}/radeontop
%{_mandir}/man1/radeontop.1.gz


%changelog
* Mon Apr 21 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-1.git20140421.eadc100
- Initial package
