<script>
  import Col from '../_components/grid/Col.svelte';
  import Grid from '../_components/grid/Grid.svelte';
  import Row from '../_components/grid/Row.svelte';

  const FORM_URL = 'https://sendmail.nymea.io/send.php';

  let response;

  async function validateAndSend() {
    // STATE.validationErrors = {}
   
    const formData = new FormData(document.forms['contact-form']);

    for (var pair of formData.entries()) {
      console.log(pair[0]+ ', ' + pair[1]); 
  }

    response = await send(formData);

    console.log('response', response);

    // const validationResult = validate(formData);
    
		// if(validationResult.isValid){
		// 	 trySendData(formData).then(data => {
		// 		STATE.send = data;
		// 		STATE.isSent = data.success;
		// 	})
		// } else {
		// 	validationResult.errors.forEach(error => {
		// 		STATE.validationErrors[error] = true
		// 	})
		// }
  }
  
  async function send(formData) {
    const response = await fetch(FORM_URL, {
      method: 'POST', 
      body: formData
    });
    return await response.text();
  }
</script>

<style>
  section {
    background-color: var(--silver-base);
    border-bottom: 1px solid var(--silver-darken-10);
    /* border-top: 1px solid var(--silver-darken-10); */
    margin: 0 0 var(--space-04);
    padding: calc(var(--space-10) + var(--space-07)) 0 calc(var(--space-10) + var(--space-09));
  }

  h1 {
    margin-bottom: var(--space-07);
    /* margin-top: var(--space-10); */
  }

  p {
    margin-bottom: var(--space-09);
  }

  form {
    margin-bottom: var(--space-10);
  }

  label {
    display: block;
    margin-bottom: var(--space-07);
  }

  span {
    display: block;
    margin: var(--space-04) 0;
  }

  input,
  textarea,
  button {
            appearance: none;
       -moz-appearance: none;
    -webkit-appearance: none;
    border: 1px solid var(--silver-darken-20);
    border-radius: 5px;
    padding: var(--space-04) var(--space-07);
  }

  input,
  textarea {
    width: 100%;
  }

  textarea {
    height: 9rem;
  }

  button {
    background-color: var(--grey-darken-40);
    color: var(--silver-base);
    display: inline-block;
    padding: var(--space-04) var(--space-07);
    text-decoration: none;
  }

  button ion-icon {
    font-size: 1.125rem;
    transform: translateX(0.375rem) translateY(0.15em);
    transition: transform 100ms ease-in-out;
  }

  button:hover ion-icon {
    transform: translateX(0.5rem) translateY(0.15em);
  }
</style>

<section>
  <Grid width={{'xs': '100%', 'sm': '100%', 'md': '64em', 'lg': '75em', 'xl': '75em'}}>
    <Row>
      <Col span={{'xs': 12, 'sm': 6, 'md': 6, 'lg': 6, 'xl': 6}} offset={{'xs': 0, 'sm': 1, 'md': 1, 'lg': 1, 'xl': 1}}>
        <form name="contact-form" id="contact-form" action={FORM_URL} method="post">
          <h1>Get in touch</h1>
          <!-- <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.</p> -->
          <div>
            <label>
              <span>Name</span>
              <input name="name" placeholder="Please enter your name" type="text" required />
            </label>
          </div>
          <div>
            <label>
              <span>Email</span>
              <input name="email" placeholder="Please enter your email address" type="email" required />
            </label>
          </div>
          <div>
            <label>
              <span>Message</span>
              <textarea name="message" placeholder="Include all the details you can" required></textarea>
            </label>
          </div>
          <div>
            <!-- {#await } -->
            <button name="submit" type="submit" id="contact-submit" on:click|preventDefault={validateAndSend}>
              Send Email
              <ion-icon name="send"></ion-icon>
            </button>
          </div>
        </form>
      </Col>
    </Row>
  </Grid>
</section>
