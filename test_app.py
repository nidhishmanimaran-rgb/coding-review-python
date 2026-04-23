from app import app

with app.test_client() as client:
    # Test the home page
    response = client.get('/')
    print(f"Home page status: {response.status_code}")
    if response.status_code != 200:
        print(f"Response: {response.data[:500]}")
    else:
        print("Home page working correctly!")
    
    # List all routes
    print("\nRegistered routes:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.rule} -> {rule.endpoint}")
