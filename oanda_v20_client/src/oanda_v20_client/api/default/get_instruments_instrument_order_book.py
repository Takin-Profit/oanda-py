from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.get_instruments_instrument_order_book_response_200 import (
    GetInstrumentsInstrumentOrderBookResponse200,
)
from ...types import Unset


def _get_kwargs(
    instrument: str,
    *,
    time: Union[Unset, str] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["Authorization"] = authorization

    if not isinstance(accept_datetime_format, Unset):
        headers["Accept-Datetime-Format"] = accept_datetime_format

    params: Dict[str, Any] = {}

    params["time"] = time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/instruments/{instrument}/orderBook".format(
            instrument=instrument,
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]:
    if response.status_code == 200:
        response_200 = GetInstrumentsInstrumentOrderBookResponse200.from_dict(
            response.json()
        )

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
) -> Response[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    instrument: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time: Union[Unset, str] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]:
    """Get Order Book

     Fetch an order book for an instrument.

    Args:
        instrument (str):
        time (Union[Unset, str]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]
    """

    kwargs = _get_kwargs(
        instrument=instrument,
        time=time,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    instrument: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time: Union[Unset, str] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]:
    """Get Order Book

     Fetch an order book for an instrument.

    Args:
        instrument (str):
        time (Union[Unset, str]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetInstrumentsInstrumentOrderBookResponse200]
    """

    return sync_detailed(
        instrument=instrument,
        client=client,
        time=time,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    ).parsed


async def asyncio_detailed(
    instrument: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time: Union[Unset, str] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Response[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]:
    """Get Order Book

     Fetch an order book for an instrument.

    Args:
        instrument (str):
        time (Union[Unset, str]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]
    """

    kwargs = _get_kwargs(
        instrument=instrument,
        time=time,
        authorization=authorization,
        accept_datetime_format=accept_datetime_format,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    instrument: str,
    *,
    client: Union[AuthenticatedClient, Client],
    time: Union[Unset, str] = UNSET,
    authorization: str,
    accept_datetime_format: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, GetInstrumentsInstrumentOrderBookResponse200]]:
    """Get Order Book

     Fetch an order book for an instrument.

    Args:
        instrument (str):
        time (Union[Unset, str]):
        authorization (str):
        accept_datetime_format (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GetInstrumentsInstrumentOrderBookResponse200]
    """

    return (
        await asyncio_detailed(
            instrument=instrument,
            client=client,
            time=time,
            authorization=authorization,
            accept_datetime_format=accept_datetime_format,
        )
    ).parsed