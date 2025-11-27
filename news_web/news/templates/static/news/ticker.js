const ticker = document.getElementById('ticker');
if (ticker) {
    ticker.addEventListener('mouseover', () => ticker.style.animationPlayState = 'paused');
    ticker.addEventListener('mouseout', () => ticker.style.animationPlayState = 'running');
}