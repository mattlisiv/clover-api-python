# Clover API Wrapper in Python #
Python client for Clover Point Of Sale [API V3](https://www.clover.com/api_docs/)

##### Provided under MIT License by Matt Lisivick.
*Note: this library may be subtly broken or buggy. The code is released under
the MIT License – please take the following message to heart:*
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## General
This is a Python client library for Clover API v3

## Installation
Installation for the package can be done via pip.

```commandline
    pip install cloverapi-python
```

## Usage

Initialize the client with your API key:

```python
from cloverapi.cloverapi_client import CloverApiClient
api_client = CloverApiClient(api_key='XXXXXXXX', merchant_id='XXXXXXXX',
                             api_url='https://apisandbox.dev.clover.com')
```

#### Making a request

Each API call should have a related method

For instance: 

GET /v3/merchants/{mId}

maps to:

```python
api_client.merchant_service.get_merchant()
```

Each main category on the Clover documentation:

- Merchants ```api_client.merchant_service```
- Cash ```api_client.cash_service```
- Customers ```api_client.customer_service```
- Employees ```api_client.employee_service```
- Inventory ```api_client.inventory_service```
- Notifications ```api_client.notification_service```
- Orders ```api_client.order_service```
- Payments ```api_client.payment_service```
- Apps ```api_client.app_service```

