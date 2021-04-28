const updateModal = (card) => {
    $("#pkImg").attr("src", card["images"]["small"]);
    let textBack = "";
    Object.entries(card["tcgplayer"]["prices"]).forEach(([rarity, rarityPrices]) => {
        textBack += `<h5>${rarity}</h5>
        <div class="row">`;
        Object.entries(rarityPrices).forEach(([quality, price]) => {
            textBack += `<div class="col-6">${quality}:</div><div class="col-6">$${price}</div>`;
        });
        textBack += "</div>";
        
    });
    $("#priceInfo").html(textBack);
    
};

$(".magnify").click(function (d) {
    let theSet = $(this).attr("id");
    console.log(theSet);
    fetch('https://api.pokemontcg.io/v2/cards/'+theSet)
        .then(response => response.json())
        .then(data => updateModal(data["data"])
        );
    $("#modal-wrapper").removeClass("hide");
});

$("#modal-wrapper").click(function (d) {

    $("#modal-wrapper").addClass("hide");
});