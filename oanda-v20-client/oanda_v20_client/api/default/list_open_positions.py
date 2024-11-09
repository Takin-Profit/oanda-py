from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_open_positions_response_200 import ListOpenPositionsResponse200
from ...types import Response


def _get_kwargs(
    account_id: str,
    *,
    authorization: str,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    headers["Authorization"] = authorization

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{account_id}/openPositions",
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ListOpenPositionsResponse200]]:
    if response.status_code == 200:
        response_200 = ListOpenPositionsResponse200.from_dict(response.json())

        return response_200
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
) -> Response[Union[Any, ListOpenPositionsResponse200]]:
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
    authorization: str,
) -> Response[Union[Any, ListOpenPositionsResponse200]]:
    """Open Positions

     List all open Positions for an Account. An open Position is a Position in an Account that currently
    has a Trade opened for it.

    Args:
        account_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListOpenPositionsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        authorization=authorization,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Optional[Union[Any, ListOpenPositionsResponse200]]:
    """Open Positions

     List all open Positions for an Account. An open Position is a Position in an Account that currently
    has a Trade opened for it.

    Args:
        account_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListOpenPositionsResponse200]
    """

    return sync_detailed(
        account_id=account_id,
        client=client,
        authorization=authorization,
    ).parsed


async def asyncio_detailed(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Response[Union[Any, ListOpenPositionsResponse200]]:
    """Open Positions

     List all open Positions for an Account. An open Position is a Position in an Account that currently
    has a Trade opened for it.

    Args:
        account_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListOpenPositionsResponse200]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        authorization=authorization,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    account_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    authorization: str,
) -> Optional[Union[Any, ListOpenPositionsResponse200]]:
    """Open Positions

     List all open Positions for an Account. An open Position is a Position in an Account that currently
    has a Trade opened for it.

    Args:
        account_id (str):
        authorization (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListOpenPositionsResponse200]
    """

    return (
        await asyncio_detailed(
            account_id=account_id,
            client=client,
            authorization=authorization,
        )
    ).parsed