%define oname tzinfo

Name:       ruby-%{oname}
Version:    1.1.0
Release:    4
Summary:    Daylight-savings aware timezone library

Group:      Development/Ruby
License:    MIT
URL:        http://tzinfo.rubyforge.org/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
TZInfo is a Ruby library that uses the standard tz (Olson) database to provide
daylight savings aware transformations between times in different time zones.


%prep

%build

%install
mkdir -p %{buildroot}%{gem_dir}
gem install --local --install-dir %{buildroot}%{gem_dir} \
            --force --rdoc %{SOURCE0}

%clean

%files
%dir %{gem_dir}/gems/%{oname}-%{version}/
%{gem_dir}/gems/%{oname}-%{version}/lib/
%{gem_dir}/gems/%{oname}-%{version}/test/
%doc %{gem_dir}/doc/%{oname}-%{version}
%doc %{gem_dir}/gems/%{oname}-%{version}/LICENSE
%doc %{gem_dir}/gems/%{oname}-%{version}/Rakefile
%doc %{gem_dir}/gems/%{oname}-%{version}/README*
%doc %{gem_dir}/gems/%{oname}-%{version}/CHANGES*
%{gem_dir}/gems/%{oname}-%{version}/.yardopts
%{gem_dir}/cache/%{oname}-%{version}.gem
%{gem_dir}/specifications/%{oname}-%{version}.gemspec
%{gem_dir}/gems/%{oname}-%{version}/*gemspec


