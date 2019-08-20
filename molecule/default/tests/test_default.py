debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']
version = '0.4.0'
service_name = 'grafana_annotations_bot'
user = 'grafana_annotations_bot'
group = 'grafana_annotations_bot'
root_dir = '/opt/grafana_annotations_bot'


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_install_dir(host):
    f = host.file(root_dir)

    assert f.exists
    assert f.is_directory


def test_service(host):
    s = host.service(service_name)

    assert s.is_enabled
    assert s.is_running


def test_user(host):
    u = host.user(user)

    assert u.shell == '/usr/sbin/nologin'


def test_group(host):
    g = host.user(group)

    assert g.exists


def test_default_template(host):
    f = host.file(root_dir + '/default.tmpl')

    assert f.exists
