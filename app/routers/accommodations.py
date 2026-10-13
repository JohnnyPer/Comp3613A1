from fastapi import HTTPException, Request
from fastapi.responses import HTMLResponse

from app.dependencies.auth import IsUserLoggedIn, get_current_user
from app.dependencies.session import SessionDep
from app.repositories.accommodation import AccommodationRepository
from app.repositories.review import ReviewRepository
from app.services.accommodation_service import AccommodationService
from app.services.review_service import ReviewService

from . import router, templates


@router.get(
    "/listings",
    response_class=HTMLResponse,
    name="explore_listings",
)
async def explore_listings(
    request: Request,
    user_logged_in: IsUserLoggedIn,
    db: SessionDep,
    search: str = "",
):
    current_user = (
        await get_current_user(request, db)
        if user_logged_in
        else None
    )

    accommodation_repo = AccommodationRepository(db)
    accommodation_service = AccommodationService(accommodation_repo)

    listings = accommodation_service.search_listings(search)

    return templates.TemplateResponse(
        request=request,
        name="listings.html",
        context={
            "listings": listings,
            "search": search,
            "current_user": current_user,
            "user": current_user,
        },
    )


@router.get(
    "/listings/{accommodation_id}",
    response_class=HTMLResponse,
    name="listing_detail",
)
async def listing_detail(
    request: Request,
    accommodation_id: int,
    user_logged_in: IsUserLoggedIn,
    db: SessionDep,
):
    current_user = (
        await get_current_user(request, db)
        if user_logged_in
        else None
    )

    accommodation_repo = AccommodationRepository(db)
    accommodation_service = AccommodationService(accommodation_repo)

    listing = accommodation_service.get_listing(accommodation_id)

    if listing is None:
        raise HTTPException(
            status_code=404,
            detail="Accommodation listing not found.",
        )

    return templates.TemplateResponse(
        request=request,
        name="listing-detail.html",
        context={
            "listing": listing,
            "current_user": current_user,
            "user": current_user,
        },
    )


@router.get(
    "/listings/{accommodation_id}/reviews",
    response_class=HTMLResponse,
    name="listing_reviews",
)
async def listing_reviews(
    request: Request,
    accommodation_id: int,
    user_logged_in: IsUserLoggedIn,
    db: SessionDep,
):
    current_user = (
        await get_current_user(request, db)
        if user_logged_in
        else None
    )

    # Retrieve the accommodation.
    accommodation_repo = AccommodationRepository(db)
    accommodation_service = AccommodationService(accommodation_repo)

    listing = accommodation_service.get_listing(accommodation_id)

    if listing is None:
        raise HTTPException(
            status_code=404,
            detail="Accommodation listing not found.",
        )

    # Retrieve reviews for this accommodation.
    review_repo = ReviewRepository(db)
    review_service = ReviewService(review_repo)

    reviews = review_service.get_reviews_for_accommodation(
        accommodation_id
    )
    average_rating = review_service.get_average_rating(reviews)

    return templates.TemplateResponse(
        request=request,
        name="listing-reviews.html",
        context={
            "listing": listing,
            "reviews": reviews,
            "average_rating": average_rating,
            "current_user": current_user,
            "user": current_user,
        },
    )