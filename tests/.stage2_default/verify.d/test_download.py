def test_git_master(host):
    assert host.ansible(
      "command",
      "cat /app/app10/code_app10/content.txt",
      become=True,
      check=False,
    )["stdout"] == "Version 2"

def test_git_version(host):
    assert host.ansible(
      "command",
      "cat /app/app11/code_app11/content.txt",
      become=True,
      check=False,
    )["stdout"] == "Version 1"

def test_url_download(host):
    assert host.ansible(
      "stat",
      "path=/app/app20/code_app20/v2.zip checksum_algorithm=md5",
      become=True,
      check=False,
    )["stat"]["checksum"] == "9318d43e63cee2c089deda0c2d1a5f40"
def test_url_unpack(host):
    assert host.ansible(
      "command",
      "cat /app/app21/code_app21/test_app-2/content.txt",
      become=True,
      check=False,
    )["stdout"] == "Version 2"
