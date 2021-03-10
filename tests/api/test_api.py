def test_todo(client):
    """Start with a blank database."""
    # setup
    expected = {"task": 'Say "Hello, World!"'}
    # execution
    rv = client.get("/api/indicators")
    # validation
    assert rv.json == expected
