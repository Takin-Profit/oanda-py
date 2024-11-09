from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.stream_pricing_response_200 import StreamPricingResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    account_id: str,
    *,
    instruments: List[str],
    snapshot: Union[Unset, bool] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["Authorization"] = authorization

    if not isinstance(accept_datetime_format, Unset):
        headers["Accept-Datetime-Format"] = accept_datetime_format

    params: Dict[str, Any] = {}

    json_instruments = instruments

    params["instruments"] = json_instruments

    params["snapshot"] = snapshot

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/pricing/stream",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, StreamPricingResponse200]]:
    if response.status_code == 200:
        response_200 = StreamPricingResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
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
) -> Response[Union[Any, StreamPricingResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    instruments: List[str],
    snapshot: Union[Unset, bool] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Response[Union[Any, StreamPricingResponse200]]:
    """Price Stream

     Get a stream of Account Prices starting from when the request is made.
    This pricing stream does not include every single price created for the Account, but instead will
    provide at most 4 prices per second (every 250 milliseconds) for each instrument being requested.
    If more than one price is created for an instrument during the 250 millisecond window, only the
    price in effect at the end of the window is sent. This means that during periods of rapid price
    movement, subscribers to this stream will not be sent every price.
    Pricing windows for different connections to the price stream are not all aligned in the same way
    (i.e. they are not all aligned to the top of the second). This means that during periods of rapid
    price movement, different subscribers may observe different prices depending on their alignment.

    Args:
        account_id (str):
        instruments (List[str]):
        snapshot (Union[Unset, bool]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StreamPricingResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        instruments=instruments,
        snapshot=snapshot,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    instruments: List[str],
    snapshot: Union[Unset, bool] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, StreamPricingResponse200]]:
    """Price Stream

     Get a stream of Account Prices starting from when the request is made.
    This pricing stream does not include every single price created for the Account, but instead will
    provide at most 4 prices per second (every 250 milliseconds) for each instrument being requested.
    If more than one price is created for an instrument during the 250 millisecond window, only the
    price in effect at the end of the window is sent. This means that during periods of rapid price
    movement, subscribers to this stream will not be sent every price.
    Pricing windows for different connections to the price stream are not all aligned in the same way
    (i.e. they are not all aligned to the top of the second). This means that during periods of rapid
    price movement, different subscribers may observe different prices depending on their alignment.

    Args:
        account_id (str):
        instruments (List[str]):
        snapshot (Union[Unset, bool]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StreamPricingResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        instruments=instruments,
        snapshot=snapshot,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    instruments: List[str],
    snapshot: Union[Unset, bool] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Response[Union[Any, StreamPricingResponse200]]:
    """Price Stream

     Get a stream of Account Prices starting from when the request is made.
    This pricing stream does not include every single price created for the Account, but instead will
    provide at most 4 prices per second (every 250 milliseconds) for each instrument being requested.
    If more than one price is created for an instrument during the 250 millisecond window, only the
    price in effect at the end of the window is sent. This means that during periods of rapid price
    movement, subscribers to this stream will not be sent every price.
    Pricing windows for different connections to the price stream are not all aligned in the same way
    (i.e. they are not all aligned to the top of the second). This means that during periods of rapid
    price movement, different subscribers may observe different prices depending on their alignment.

    Args:
        account_id (str):
        instruments (List[str]):
        snapshot (Union[Unset, bool]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, StreamPricingResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        instruments=instruments,
        snapshot=snapshot,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    instruments: List[str],
    snapshot: Union[Unset, bool] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, StreamPricingResponse200]]:
    """Price Stream

     Get a stream of Account Prices starting from when the request is made.
    This pricing stream does not include every single price created for the Account, but instead will
    provide at most 4 prices per second (every 250 milliseconds) for each instrument being requested.
    If more than one price is created for an instrument during the 250 millisecond window, only the
    price in effect at the end of the window is sent. This means that during periods of rapid price
    movement, subscribers to this stream will not be sent every price.
    Pricing windows for different connections to the price stream are not all aligned in the same way
    (i.e. they are not all aligned to the top of the second). This means that during periods of rapid
    price movement, different subscribers may observe different prices depending on their alignment.

    Args:
        account_id (str):
        instruments (List[str]):
        snapshot (Union[Unset, bool]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, StreamPricingResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            instruments=instruments,
            snapshot=snapshot,
            authorization=authorization,
            accept_datetime_format=accept_datetime_format,
        )
    ).parsed
