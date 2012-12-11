%define oname tzinfo

Name:       ruby-%{oname}
Version:    0.3.33
Release:    1
Summary:    Daylight-savings aware timezone library
Group:      Development/Ruby
License:    MIT
URL:        http://tzinfo.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRequires: rubygems
BuildArch:  noarch
%rename     rubygem-%{oname}

%description
TZInfo is a Ruby library that uses the standard tz (Olson) database to provide
daylight savings aware transformations between times in different time zones.


%prep

%build

%install
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
rm -rf %{buildroot}%{ruby_gemdir}/cache

%files
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/test/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Fri May 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.3.33-1
+ Revision: 796012
- update to 0.3.33
- rename to comply ruby packaging policy

* Mon Dec 20 2010 Rémy Clouard <shikamaru@mandriva.org> 0.3.23-1mdv2011.0
+ Revision: 623427
- import rubygem-tzinfo

