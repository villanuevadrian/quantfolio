def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_portfolio(client, test_user):
    response = client.post(
        "/portfolios/",
        json={
            "asset_type": "Stock",
            "name": "Test_portfolio",
            "owner": str(test_user.user_id),
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test_portfolio"
    assert data["asset_type"] == "Stock"
    assert data["owner"] == str(test_user.user_id)
