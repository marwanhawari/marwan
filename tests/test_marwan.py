from marwan.main import main


def test_main(capsys):
    main(["-lpwg"])

    out, err = capsys.readouterr()
    assert (
        out
        == """Opening https://www.github.com/marwanhawari/
Opening https://www.linkedin.com/in/marwanhawari/
Opening https://pypi.org/user/marwanhawari/
Opening https://www.marwanhawari.com/\n"""
    )
    assert err == ""
