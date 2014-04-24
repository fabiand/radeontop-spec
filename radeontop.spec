%global commit eadc100956fb5e346a4c5726453efd15fb2ec9f7
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global checkout .20140421git%{shortcommit}

Summary:    View GPU utilization off AMD/ATI Radeon devices
Name:       radeontop
Version:    0.7
Release:    2%{?checkout}%{?dist}
License:    GPLv3
Group:      System Environment/Libraries
URL:        https://github.com/clbr/%{name}

Source0:    %{url}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz

BuildRequires: asciidoc gettext
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(pciaccess)
BuildRequires: pkgconfig(libdrm)

%description
RadeonTop shows the utilization of your GPU, both in general and by blocks.

Supported cards are R600 and up.


%prep
%setup -q -n %{name}-%{commit}

# Prevent recompile on make install
# Issue: https://github.com/clbr/radeontop/issues/9
sed -i '/install:/ s/ all//' Makefile


%build
# configure doesn't exist, but we need the exported CFLAGS and friends
%configure || :

# plain=1 prevents stripping
# CC="..." to also pass -g
# Patch: https://github.com/clbr/radeontop/pull/8
make radeontop %{?_smp_mflags} PREFIX=%{_prefix} plain=1


%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}
%find_lang %{name}


%files -f %{name}.lang
%doc README.md TODO COPYING
%{_sbindir}/radeontop
%{_mandir}/man1/radeontop.1*


%changelog
* Thu Apr 24 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-2.20140421giteadc100
- Fix commit position, BuildRequirements, build, and man page inclusion (thanks mschwendt)

* Mon Apr 21 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 0.7-1.git20140421.eadc100
- Initial package
