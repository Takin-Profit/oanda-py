from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.set_trade_dependent_orders_body import SetTradeDependentOrdersBody
from ...models.set_trade_dependent_orders_response_200 import SetTradeDependentOrdersResponse200
from ...models.set_trade_dependent_orders_response_400 import SetTradeDependentOrdersResponse400
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    trade_specifier: str,
    *,
    body: SetTradeDependentOrdersBody,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["Authorization"] = authorization

    if not isinstance(accept_datetime_format, Unset):
        headers["Accept-Datetime-Format"] = accept_datetime_format

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/accounts/{account_id}/trades/{trade_specifier}/orders",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]:
    if response.status_code == 200:
        response_200 = SetTradeDependentOrdersResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = SetTradeDependentOrdersResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    trade_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetTradeDependentOrdersBody,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]:
    """Set Dependent Orders

     Create, replace and cancel a Trade's dependent Orders (Take Profit, Stop Loss and Trailing Stop
    Loss) through the Trade itself

    Args:
        account_id (str):
        trade_specifier (str):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):
        body (SetTradeDependentOrdersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        trade_specifier=trade_specifier,
        body=body,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    trade_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetTradeDependentOrdersBody,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]:
    """Set Dependent Orders

     Create, replace and cancel a Trade's dependent Orders (Take Profit, Stop Loss and Trailing Stop
    Loss) through the Trade itself

    Args:
        account_id (str):
        trade_specifier (str):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):
        body (SetTradeDependentOrdersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]
    """

    return sync_detailed(
        account_id=account_id,
        trade_specifier=trade_specifier,
        client=client,
        body=body,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    trade_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetTradeDependentOrdersBody,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]:
    """Set Dependent Orders

     Create, replace and cancel a Trade's dependent Orders (Take Profit, Stop Loss and Trailing Stop
    Loss) through the Trade itself

    Args:
        account_id (str):
        trade_specifier (str):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):
        body (SetTradeDependentOrdersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        trade_specifier=trade_specifier,
        body=body,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    trade_specifier: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SetTradeDependentOrdersBody,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]]:
    """Set Dependent Orders

     Create, replace and cancel a Trade's dependent Orders (Take Profit, Stop Loss and Trailing Stop
    Loss) through the Trade itself

    Args:
        account_id (str):
        trade_specifier (str):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):
        body (SetTradeDependentOrdersBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SetTradeDependentOrdersResponse200, SetTradeDependentOrdersResponse400]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            trade_specifier=trade_specifier,
            client=client,
            body=body,
            authorization=authorization,
            accept_datetime_format=accept_datetime_format,
        )
    ).parsed