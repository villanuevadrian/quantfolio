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


def test_get_portfolio_not_found(client):
    fake_id = "00000000-0000-0000-0000-000000000000"
    response = client.get(f"/portfolios/{fake_id}")
    assert response.status_code == 404


def test_get_portfolio(client, test_user):
    response = client.post(
        "/portfolios/",
        json={
            "asset_type": "Stock",
            "name": "Test_portfolio",
            "owner": str(test_user.user_id),
        },
    )
    created = response.json()
    portfolio_id = created["portfolio_id"]

    response = client.get(f"/portfolios/{portfolio_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["portfolio_id"] == portfolio_id
    assert data["name"] == "Test_portfolio"
    assert data["asset_type"] == "Stock"


def test_list_portfolios_by_user(client, test_user):
    response = client.post(
        "/portfolios/",
        json={
            "asset_type": "Stock",
            "name": "Test_portfolio",
            "owner": str(test_user.user_id),
        },
    )
    created = response.json()
    user_id = created["owner"]

    response = client.get(f"/portfolios/?user_id={user_id}")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["owner"] == str(test_user.user_id)
    assert data[0]["name"] == "Test_portfolio"
